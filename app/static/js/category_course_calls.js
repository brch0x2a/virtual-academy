function fillHtmlElements(){
  initCategoryCourseCollection("category");
}

$( document ).ready(
  function(){
    importScript('category_course_actions',fillHtmlElements); 
  }
);

function edit(id){
  console.log("id: "+id);
  initCategoryCourseCollection("ucategory");
  $.getJSON("/getCourseById?courseId="+id, data =>{
    let obj = data;
    console.log("\n\n\n\nOBJ",obj[0]);
    $("input[name='utitle']").val(obj[0].title);
    $("#udescription").val(obj[0].description);
    $("input[name='uid']").val(obj[0].id);
    $("#editCover").attr("src", obj[0].image);
    $("#category").val(obj[0].description);
  });
}

function deleteE(id){
  console.log(id);
  $.getJSON("/deleteCourse?id="+id, data=>{
    window.location.reload(true);
  });
}
