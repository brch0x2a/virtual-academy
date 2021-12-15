function fillHtmlElements(){
  initCategoryCourseCollection("branch");
  initCategoryCourseCollection("ubranch");
}

$( document ).ready(
  function(){
    importScript('BE_COMUNICATION/category_course_actions',fillHtmlElements); 
  }
);

function deleteE(id){
  deleteCategoryCourseE(id);
}

function fillEditForm(categoryCourse){
  // console.log("categoryCourse DATA: ", categoryCourse);
  $("input[name='utitle']").val(categoryCourse[0].name);
  $("input[name='uid']").val(categoryCourse[0].id);
  $("input[name='ubranch']").val(categoryCourse[0].id_branch);
}

function edit(id){
  getCategoryCourseE(id, fillEditForm);
}