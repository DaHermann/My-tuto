**Passport Local Mongoose authentification**


  1- Installation des dependances

      npm install passport passport-local passport-local-mongoose mongoose

  2- Configurer Mongoose pour Utiliser Passport dans userModel.js

    const mongoose = require('mongoose');
    const Schema = mongoose.Schema;
    const passportLocalMongoose = require('passport-local-mongoose');
      
    const User = new Schema({
        email: {
          type: String, 
          required:true, 
          unique:true,
          validate: {
              validator: () => {Promise.resolve(false)},
              message: 'Email validation failed'
          }
      }, 
      username : {
          type: String, 
          unique: true, 
          required:true
      }, });
      
    User.plugin(passportLocalMongoose);
    module.exports = mongoose.model('User', User);
    
 3- configuratioin de la page App.js

    const express = require('express');
    const expressSession = require('express-session');
    const path =  require('path');
    const app = express();
    const passport = require('passport');
    const LocalStrategy = require('passport-local').Strategy;
    const mongoose = require('mongoose');
    const User = require('./userModel');
    const uri = "mongodb://username:password@localhost/myDB";


        /**
       * Database connection
       */
      
      const connectToDB = async () => {
          try {
              await mongoose.connect(uri, {
                  autoIndex: true
              })
              console.log('Connected to Mongodb Atlas');
          } catch (error) {
              console.error(error);
          }
      }
      connectToDB();



    app.use(expressSession({ secret: 'keyboard cat', resave: true, saveUninitialized: true }));
    //Passport Local Strategie for Mongoose
    passport.use(new LocalStrategy(User.authenticate()));
    app.use(passport.initialize()); 
    app.use(passport.session());

    // use static authenticate method of model in LocalStrategy
    passport.use(new LocalStrategy(User.authenticate()));
    
    // use static serialize and deserialize of model for passport session support
    passport.serializeUser(User.serializeUser());
    passport.deserializeUser(User.deserializeUser());

4- Configuration des routes userRoutes.js

    const express = require('express');
    const Router = express.Router();
    const {LogIn, LogOut, SingUp, GetSingUpPage, GetLoginPage}  =  require('./userControllers');
    
    
    Router.get('/', GetLoginPage)
    Router.get('/singup', GetSingUpPage)
    // Logout
    Router.get('/logout', LogOut);

    // Authentification d'un User
    Router.post('/login',LogIn)
    //Enregistrement de User
    Router.post('/singup',SingUp)

    

5- Configuration du controller.js

  * Enregister un user

        const SingUp = async (req, res) => {
            const {username,email, password} = req.body;
          
            const newUser = new User({email: email, username : username});
          
            await User.register(newUser, password, function(err, user) { 
              if (err) { 
                res.json({success:false, message:"Your account could not be saved Error: ", err}) 
              }else{ 
            //   res.json({success: true, message: "Your account has been saved"});
                console.log("User : ", user);
                res.redirect('/fruit/')
              } 
            }); 
          
          }
  
      

*  Authentifier un user

        const LogIn = async (req, res) => {

          const {username, password} = req.body;
            
            if(!username){ 
                res.json({success: false, message: "Username was not given"}) 
              } else { 
                if(!password){ 
                  res.json({success: false, message: "Password was not given"}) 
                }else{ 
                  passport.authenticate('local', function (err, user, info) { 
                    console.log('User Is : ', user);
                    if(err){ 
                      res.json({success: false, message: err}) 
                    } else{ 
                      if (! user) { 
                        res.json({success: false, message: 'username or password incorrect'}) 
                      } else{ 
                        req.login(user, function(err){ 
                          if(err){ 
                            res.json({success: false, message: err}) 
                          }else{ 
                            // const token = jwt.sign({userId : user._id, username:user.username}, secretkey, {expiresIn: '24h'}) 
                            // res.json({success:true, message:"Authentication successful", token: token }); 
                            res.redirect("/");
                          } 
                        }) 
                      } 
                    } 
                  })(req, res); 
                } 
              };     
        }


      * passport.authenticate('local',fn)(req, res) 
      * req.login(user, fn)
 
      * Verifier qu'un utilisateur est authentifié

            const GetLoginPage = (req, res) => {     
              if (req.isAuthenticated()) {
                res.redirect('/');
              } else {
                res.render('/login');
              } 
            }
      * Deconnexion de l'user

              const LogOut = async (req, res) => {
                req.logout(() => {console.log("Logout")});
                res.redirect("/user");
              }
  
    

    




