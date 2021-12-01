// function getCourseById(id, callBackFunction){
//     // console.log("id: "+id);
//     $.getJSON("/getCourseById?courseId="+id, data =>{
//     callbackHandler(callBackFunction, data);
//     });
// }
  
function getModuleE(moduleId,callBackFunction){
    // console.log("id: "+moduleId);
    $.getJSON("/getModuleE?id="+moduleId, data =>{
        callbackHandler(callBackFunction, data);
    });
}

function deleteModuleE(id){
    // console.log(id);
    $.getJSON("/deleteModule?id="+id, data=>{
      window.location.reload(true);
    });
  }