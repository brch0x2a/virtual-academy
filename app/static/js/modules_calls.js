function fillHtmlElements(){
  initCategoryCourseCollection('category');
  initCategoryCourseCollection('ucategory');
}

$( document ).ready(
  function(){
    importScript('BE_COMUNICATION/course_actions');
    importScript('BE_COMUNICATION/module_actions');
    importScript('BE_COMUNICATION/category_course_actions',fillHtmlElements);  
  }
);

function fillSelect(selectIdB, data){
  // console.log("fillSelect: \nselectB: ", selectIdB,"\ncourses: ", data);
  let  select = document.getElementById(selectIdB);
  select.options.length = 0;
  data.forEach(element => {
    select.options[select.options.length] = new Option(element.title, element.id);
  });
}

function triggerCourse(selectIdA, selectIdB){
  let option  = document.getElementById(selectIdA).value;
  // console.log("triggerCourse");
  getCourseByCategoryId(option,
    function(data){
    fillSelect(selectIdB,data);
  });
}
 
function fillEditForm(module){
  $("input[name='utitle']").val(module[0].title);
  $("input[name='uprice']").val(module[0].price);
  $("input[name='uid']").val(module[0].id);
}

function edit(id){
  initCategoryCourseCollection("ucategory");
  getModuleE(id, fillEditForm);
}
  
function deleteE(id){
  deleteModuleE(id);
}