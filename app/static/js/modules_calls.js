// function initCategoryCollection(selectId){
//     console.log("id: "+selectId);
//     $.getJSON("/category_course", data =>{
//       let obj = data;
//       console.log("SELCT ID: ", selectId, "obj: ", obj);
//       let  select = document.getElementById(selectId);
//       select.options.length = 0;
//       obj.forEach(element => {
//         select.options[select.options.length] = new Option(element.name, element.id);
//       });
//     });
// }

function fillHtmlElements(){
  initCategoryCourseCollection('category');
  initCategoryCourseCollection('ucategory');
}

$( document ).ready(
  function(){
    importScript('BE_COMUNICATION/course_actions');
    importScript('BE_COMUNICATION/category_course_actions',fillHtmlElements);  
  }
);

function fillSelect(selectIdB, data){
  console.log("fillSelect: \nselectB: ", selectIdB,"\ncourses: ", data);
  let  select = document.getElementById(selectIdB);
  select.options.length = 0;
  data.forEach(element => {
    select.options[select.options.length] = new Option(element.title, element.id);
  });
}

function triggerCourse(selectIdA, selectIdB){
  let option  = document.getElementById(selectIdA).value;
  console.log("triggerCourse");
  getCourseByCategoryId(option,
    function(data){
    fillSelect(selectIdB,data);
  });
}
  
function edit(id){
  console.log("id: "+id);
  initCategoryCourseCollection("ucategory");
  $.getJSON("/getModuleE?id="+id, data =>{
    let obj = data;
    console.log("EDIT DATA: ",obj);
    $("input[name='utitle']").val(obj[0].title);
    $("input[name='uprice']").val(obj[0].price);
    $("input[name='uid']").val(obj[0].id);
  });
}
  
function deleteE(id){
  console.log(id);
  $.getJSON("/deleteModule?id="+id, data=>{
    window.location.reload(true);
  });
}