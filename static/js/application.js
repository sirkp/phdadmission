function CheckCountry(val){
  var element1=document.getElementById('id_state_div');
  var element2=document.getElementById('id_state_description_div');
  if(val=='India'){
    element1.style.display='block';
    element2.style.display='none';
  }
  else{
    element2.style.display='block';
    element1.style.display='none';
  }
}

function CheckCategory(val){
  var element=document.getElementById('id_category_other_div');
  if(val=='Other'){
    element.style.display='block';
  }
  else{
    element.style.display='none';
  }
}

function CheckUGDiscipline(val){
  var element=document.getElementById('id_ug_discipline_other_div');
  if(val=='Other'){
    element.style.display='block';
  }
  else{
    element.style.display='none';
  }
}

function CheckPGDiscipline(val){
  var element=document.getElementById('id_pg_discipline_other_div');
  if(val=='Other'){
    element.style.display='block';
  }
  else{
    element.style.display='none';
  }
}

function CheckResearchArea(val){
  var element=document.getElementById('id_research_area_other_div');
  if(val=='Other'){
    element.style.display='block';
  }
  else{
    element.style.display='none';
  }
}

function CheckTypeOfWork(val){
  var element=document.getElementById('id_type_of_work_other_div');
  if(val=='Other'){
    element.style.display='block';
  }
  else{
    element.style.display='none';
  }
}

function CheckQEDiscipline(val){
  var element=document.getElementById('id_qe_discipline_other_div');
  if(val=='Other'){
    element.style.display='block';
  }
  else{
    element.style.display='none';
  }
}
