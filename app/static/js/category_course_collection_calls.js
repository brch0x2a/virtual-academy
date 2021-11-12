function initCategoryCollection(selectId){
  console.log("id from jquery function: "+selectId);
  $.getJSON("/branch_of_kwnoledge_all", data =>{
    console.log("data: ", data);
    let obj = data;
    // console.log("OBJETO1: ", obj);
    let  select = document.getElementById(selectId);
    select.options.length = 0;
    console.log("OBJETO: ", obj);
    obj.forEach(element => {
    console.log("ELEMENTO: ", element);
    select.options[select.options.length] = new Option(element.name, element.id);
    }); 
  });
}

function edit(id){
  console.log("editing --> id: "+id);
  $.getJSON("/getCategoryCourseE?id="+id, data =>{
    let obj = data;
    console.log(obj[0]);
    $("input[name='utitle']").val(obj[0].name);
    $("input[name='uid']").val(obj[0].id);
    $("#ubranch").val(obj[0].id_branch);
  });
}

function deleteE(id){
  console.log(id);
  $.getJSON("/delete_category_course?id="+id, data=>{
    window.location.reload(true);
  });
}

initCategoryCollection("branch");
initCategoryCollection("ubranch");