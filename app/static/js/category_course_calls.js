    function initCategoryCollection(selectId){

      $.getJSON("/category_course", data=>{
        // Work with JSON data here

        // let obj = JSON.parse(data);
        let obj = data;

        let  select = document.getElementById(selectId);

        select.options.length = 0;

        obj.forEach(element => {
          select.options[select.options.length] = new Option(element.name, element.id);
        }); 

      });

    }


    function edit(id){
    console.log("id: "+id);

    initCategoryCollection("ucategory");

    $.getJSON("/getCourseById?courseId="+id, data =>{
      // let obj = JSON.parse(data);
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

  initCategoryCollection("category");