/*
* Settings for buttons bar within snippet admin
*/
DCM_Buttons_settings = [
    {name:'Maximize', id: 'FullscreenEnter', classname: 'dcm-icons-fullscreen_enter', funcname:"maximize_editor", method:"internal" },
    {name:'Normal size', id: 'FullscreenExit', classname: 'dcm-icons-fullscreen_exit', funcname:"normalize_editor", method:"internal" },
    {separator:true},
    {name:'Undo', id: 'Undo', classname: 'dcm-icons-arrow_undo', funcname:"do_undo", method:"internal" },
    {name:'Redo', id: 'Redo', classname: 'dcm-icons-arrow_redo', funcname:"do_redo", method:"internal" },
    {separator:true},
    {name:'Help', id: 'Help', classname: 'dcm-icons-help', funcname:"externalressource" },
    {name:'Settings', id: 'Settings', classname: 'dcm-icons-cog_edit', funcname:"show_settings", method:"internal" }
];
