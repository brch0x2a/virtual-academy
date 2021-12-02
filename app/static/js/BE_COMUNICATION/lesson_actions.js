function deleteLessonE(lessonId){
  // console.log(id);
  $.getJSON("/deleteLesson?id="+id, data=>{
    window.location.reload(true);
  });
}


