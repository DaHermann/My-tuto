# Configure Bridge

## IN `/confbrigde.conf`

    ; --- ConfBridge User Profile Options ---

    [default_user]
    type=user
    music_on_hold_when_empty=yes
    music_on_hold_class=default
    announce_user_count_all=yes
    announce_join_leave=yes
    dsp_drop_silence=yes
    denoise=yes
    pin=123

    [default_admin]
    type=user
    admin=yes
    music_on_hold_when_empty=yes
    music_on_hold_class=default
    announce_user_count_all=yes
    announce_join_leave=yes
    dsp_drop_silence=yes
    denoise=yes
    pin=123

    ; --- ConfBridge Bridge Profile Options ---
    [default_bridge]
    type=bridge
    max_members=50
    language=fr
    
    
    
    ## IN `extension.conf`
    
        ;===================================== VoiceMailMain
        
        exten => 200,1,NoOp(## Bridge ##)
        same => n,ConfBridge(1,default_bridge,default_user)
        
        
