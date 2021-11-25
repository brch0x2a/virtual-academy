function getBranchOfKnowledgeE(id, callBackFunction){
  $.getJSON("/branch_of_kwnoledgeE?id="+id, data =>{
    let obj = data;
    // console.log("OBJ",obj);
    // $("input[name='utitle']").val(obj[0].name);
    // $("input[name='uid']").val(obj[0].id);
    // $("#editCover").attr("src", obj[0].image);
    // $("#uimage").val(obj[0].image);
    callBackFunction(obj);
  });
}

function deleteBranchOfKnowledgeE(id){
  $.getJSON("/delete_branch_of_kwnoledge?id="+id, data=>{
    window.location.reload(true);
  });
}


