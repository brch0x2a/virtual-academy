function getCourseById(id, callBackFunction){
    // console.log("id: "+id);
    $.getJSON("/getCourseById?courseId="+id, data =>{
      let obj = data;
    callBackFunction(obj);
    });
}
  
function deleteCourseE(id){
    // console.log(id);
    $.getJSON("/deleteCourse?id="+id, data=>{
        window.location.reload(true);
    });
}