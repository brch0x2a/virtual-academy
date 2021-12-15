function fillHtmlElements(){
  initCategoryCourseCollection("category");
}

$( document ).ready(
  function(){
    importScript('BE_COMUNICATION/course_actions');
    importScript('BE_COMUNICATION/category_course_actions',fillHtmlElements); 
  }
);

function fillEditForm(course){
  $("input[name='utitle']").val(course[0].title);
  $("#udescription").val(course[0].description);
  $("input[name='uid']").val(course[0].id);
  $("#editCover").attr("src", course[0].image);
  $("#category").val(course[0].description);
}

function edit(id){
  // console.log("id: "+id);
  initCategoryCourseCollection("ucategory");
  getCourseById(id, fillEditForm);
}

function deleteE(id){
  deleteCourseE(id);
}
