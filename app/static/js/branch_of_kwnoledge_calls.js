
$( document ).ready(
  function(){
    importScript('BE_COMUNICATION/branch_of_knowledge_actions'); 
  }
);

function fillEditForm(branchOfKnowledge){
  $("input[name='utitle']").val(branchOfKnowledge[0].name);
  $("input[name='uid']").val(branchOfKnowledge[0].id);
  $("#editCover").attr("src", branchOfKnowledge[0].image);
}

function edit(id){
  getBranchOfKnowledgeE(id, fillEditForm);
}

function deleteE(id){
  deleteBranchOfKnowledgeE(id);
}