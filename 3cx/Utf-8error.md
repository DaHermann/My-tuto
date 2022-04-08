# Error during 3cx installation on debian



          System.Exception: Error in CreatingCloudServerManagementDatabase.sql: 22023: new encoding (UTF8) is
          incompatible with the encoding of the template database (SQL_ASCII) ---> Npgsql.PostgresException: 22023: new encoding (UTF8) is
          incompatible with the encoding of the template database (SQL_ASCII) at Npgsql.NpgsqlConnector.DoReadMessage(DataRowLoadingMode dataRowLoadingMode,
          Boolean isPrependedMessage) at Npgsql.NpgsqlConnector.ReadMessageWithPrepended(DataRowLoadingMode dataRowLoadingMode) at 
          Npgsql.NpgsqlDataReader.NextResultInternal() at Npgsql.NpgsqlDataReader.NextResult() at Npgsql.NpgsqlCommand.Execute(CommandBehavior behavior) at 
          Npgsql.NpgsqlCommand.ExecuteScalarInternal() at PostInstall.DBConnection.ExecuteScriptInternal(NpgsqlConnection connection, String sqlQuery, 
          IDictionary`2 parameters) at PostInstall.DBConnection.ExecuteScript(String sqlQuery, IDictionary`2 parameters) at 
          _3CXCloudDBManager.DbConnectionExtensions.ExecuteScript(IDBConnection connection, Object configurationStructure, String scriptText, Boolean 
          asResourceName) --- End of inner exception stack trace --- at _3CXCloudDBManager.DbConnectionExtensions.ExecuteScript(IDBConnection connection,
          Object configurationStructure, String scriptText, Boolean asResourceName) at _3CXCloudDBManager.CloudDBManager.
          CreateCloudServerManagementDatabase(IDBConnection superuser, CloudServerManagementDatabaseConfiguration configuration)
          at PostInstall.SetupExecutor.CreateDatabase(Action`1 stateChanged) at PostInstall.SetupExecutor.ExecuteSetup(SetupSettings setupSettings, 
          Action`1 stateChanged) at PbxWebConfigTool.PbxSetupService.CreatePbxInternal(SetupSettings settings)
          
          
          
## If you got this installation's error, dont worry


Juste run these following commands solve the problem


   * unstall **locales**

          sudo apt-get purge locales
          
          
  *  Update your reposi it 

          sudo apt-get udate

   * then  reinstall it 

          sudo apt-get install locales

   * Now reconf it with this command

          sudo dpkg-reconfigure locales

   and chose

          en_US.UTF-8


Allright reboot your debian machine now. that is solved
