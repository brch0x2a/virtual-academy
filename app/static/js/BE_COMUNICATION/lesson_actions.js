function deleteLessonE(lessonId){
  // console.log(id);
  $.getJSON("/deleteLesson?id="+lessonId, data=>{
    window.location.reload(true);
  });
}


