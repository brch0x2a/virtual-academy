function importScript( src, callBackFunction=undefined ) {
    var baseImport = "public/js/"+src+".js"
    var script = document.createElement( 'script' );
    script.setAttribute( 'src', baseImport );
    document.body.appendChild( script );
    // console.log(`File: ${src} imported successfully`);
    script.addEventListener('load', () => {
        if (typeof callBackFunction === 'undefined'){
            return;
        }else{
            callBackFunction();
        }
    })
}

function callbackHandler(callBackFunction,data) {
    callBackFunction(data);
}