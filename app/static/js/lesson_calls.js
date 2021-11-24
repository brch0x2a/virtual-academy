// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
// playerVars = {cc_load_policy:1,autoplay:0,controls:1,enablejsapi:1,iv_load_policy:3,modestbranding:1,showinfo:0,rel:0,autohide:0,fs:1,disablekb:0,playsinline:1}
var video_player_array = document.getElementsByClassName("video")
var playerInfoList = []
for (let i = 0; i < video_player_array.length; i++) {
  const element = video_player_array[i];
  let obj = {id: element.id, videoId: element.dataset.video};
  console.log(obj);
  playerInfoList.push(obj);
}
    
function onYouTubeIframeAPIReady() {
  if(typeof playerInfoList === 'undefined'){
    return;
  } 
  for(var i = 0; i < playerInfoList.length;i++) {
    var curplayer = createPlayer(playerInfoList[i]);
  }   
}

function createPlayer(playerInfo) {
  return new YT.Player(playerInfo.id, {
    height: '200',
    width: '300',
    videoId: playerInfo.videoId,
    playerVars: {
      'cc_load_policy':1,
      'autoplay':1,
      'controls':1,
      'enablejsapi':1,
      'iv_load_policy':3,
      'modestbranding':1,
      'showinfo':0,
      'rel':0,
      'autohide':0,
      'fs':1,
      'disablekb':0,
      'playsinline':1,
    },
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
      }
    });
}

// cc_load_policy:1,autoplay:0,controls:1,enablejsapi:1,iv_load_policy:3,modestbranding:1,showinfo:0,rel:0,autohide:0,fs:1,disablekb:0,playsinline:1
// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
  event.target.playVideo();
}

// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.
var done = false;
function onPlayerStateChange(event) {
  if (event.data == YT.PlayerState.PLAYING && !done) {
    setTimeout(stopVideo, 6000);
    done = true;
  }
}

function stopVideo() {
  player.stopVideo();
}

function set_lecture(path){
  //// upload_folder /docs/  m.reading_path #toolbar=0
  document.getElementById('lecture_frame').src = path
  document.getElementById('lecture_frame').hidden = false;
  document.getElementById('player').hidden = true;
  console.log(path);
}

function set_video(video_id){
  document.getElementById('lecture_frame').hidden = true;
  document.getElementById('player').hidden = false;
  console.log(video_id);
  player.videoId = video_id;
}

// function initCategoryCollection(selectId){
//     console.log("id: "+selectId);
//     $.getJSON("/category_course", data =>{
//       let obj = data;
//       let  select = document.getElementById(selectId);
//       select.options.length = 0;
//       obj.forEach(element => {
//         select.options[select.options.length] = new Option(element.name, element.id);
//       });
//     });
// }

function triggerNext(selectIdA, selectIdB){
    let option  = document.getElementById(selectIdA).value;
    $.getJSON("/getCourseBy?"+"categoryId="+option, data =>{
      let obj = data;
      let  select = document.getElementById(selectIdB);
      select.options.length = 0;
      obj.forEach(element => {
        select.options[select.options.length] = new Option(element.title, element.id);
      });
    });
}

function triggerNextNext(selectIdA, selectIdB){
  let option  = document.getElementById(selectIdA).value;
  $.getJSON("/getModuleBy?"+"id="+option, data =>{
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
    let obj = data;
    console.log(obj[0]);
    $("input[name='utitle']").val(obj[0].title);
    $("input[name='uprice']").val(obj[0].price);
    $("input[name='uid']").val(obj[0].id);
  });
}

initCategoryCollection('category');
initCategoryCollection('ucategory');

function deleteE(id){
  console.log(id);
  $.getJSON("/deleteLesson?id="+id, data=>{
    window.location.reload(true);
  });
}
