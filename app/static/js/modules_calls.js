function initCategoryCollection(selectId){
    console.log("id: "+selectId);

    $.getJSON("/category_course", data =>{
      // let obj = JSON.parse(data);
      let obj = data;
      console.log("SELCT ID: ", selectId, "obj: ", obj);

      let  select = document.getElementById(selectId);
      select.options.length = 0;

      obj.forEach(element => {
        select.options[select.options.length] = new Option(element.name, element.id);
      });
      
    });
}

  function triggerCourse(selectIdA, selectIdB){
    let option  = document.getElementById(selectIdA).value;
    $.getJSON("getCourseBy?"+"categoryId="+option, data =>{
        // let obj = JSON.parse(data);
        let obj = data;
  
        let  select = document.getElementById(selectIdB);
        select.options.length = 0;

        obj.forEach(element => {
          select.options[select.options.length] = new Option(element.title, element.id);
   
        });
      
    });
}
  
  
  function edit(id){
        console.log("id: "+id);
  
        initCategoryCollection("ucategory");
  
  
        $.getJSON("/getModuleE?id="+id, data =>{
          // let obj = JSON.parse(data);
          let obj = data;
          console.log(obj[0]);
  
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
  
  initCategoryCollection('category');
  initCategoryCollection('ucategory');