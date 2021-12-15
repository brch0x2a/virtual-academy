function initCategoryCourseCollection(selectId){
    // console.log("id: "+selectId);
    $.getJSON("/category_course", data =>{
      let obj = data;
      // console.log("SELCT ID: ", selectId, "obj: ", obj);
      let  select = document.getElementById(selectId);
      select.options.length = 0;
      obj.forEach(element => {
        select.options[select.options.length] = new Option(element.name, element.id);
      });
    });
}

function deleteCategoryCourseE(id){
  // console.log(id);
  $.getJSON("/delete_category_course?id="+id, data=>{
    window.location.reload(true);
  });
}

function getCategoryCourseE(id,callBackFunction){
  // console.log("editing --> id: "+id);
  $.getJSON("/getCategoryCourseE?id="+id, data =>{
    callbackHandler(callBackFunction, data);
  });
}


