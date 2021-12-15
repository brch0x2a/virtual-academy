function getBranchOfKnowledgeE(id, callBackFunction){
  $.getJSON("/branch_of_kwnoledgeE?id="+id, data =>{
    callbackHandler(callBackFunction, data);
  });
}

function deleteBranchOfKnowledgeE(id){
  $.getJSON("/delete_branch_of_kwnoledge?id="+id, data=>{
    window.location.reload(true);
  });
}


