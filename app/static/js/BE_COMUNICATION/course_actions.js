function getCourseById(id, callBackFunction){
    // console.log("id: "+id);
    $.getJSON("/getCourseById?courseId="+id, data =>{
    callbackHandler(callBackFunction, data);
    });
}
  
function deleteCourseE(id){
    // console.log(id);
    $.getJSON("/deleteCourse?id="+id, data=>{
        window.location.reload(true);
    });
}

function getCourseByCategoryId(categoryId,callBackFunction){
    $.getJSON("getCourseBy?"+"categoryId="+categoryId, data =>{ 
        callbackHandler(callBackFunction, data);
    });
}