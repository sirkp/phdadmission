$(document).ready(function() {

    $("#id_scale_of_score_ug").change(function() {
        var val = $(this).val();
        if (val == "0-5 CGPA") {
            $("#id_score_ug").html("<option value=''>Select</option><option value='0-1'>0-1</option><option value='1-2'>1-2</option><option value='2-3'>2-3</option><option value='3-4'>3-4</option><option value='4-5'>4-5</option>");
        } else if (val == "0-10 CGPA") {
            $("#id_score_ug").html("<option value=''>Select</option><option value='0-1'>0-1</option><option value='1-2'>1-2</option><option value='2-3'>2-3</option><option value='3-4'>3-4</option><option value='4-5'>4-5</option><option value='5-6'>5-6</option><option value='6-7'>6-7</option><option value='7-8'>7-8</option><option value='8-9'>8-9</option><option value='9-10'>9-10</option>");

        } else if (val == "0-100%") {
            $("#id_score_ug").html("<option value=''>Select</option><option value='0-10'>0-10</option><option value='10-20'>1-20</option><option value='20-30'>20-30</option><option value='30-40'>30-40</option><option value='40-50'>40-50</option><option value='50-60'>50-60</option><option value='60-70'>60-70</option><option value='70-80'>70-80</option><option value='80-90'>80-90</option><option value='90-100'>90-100</option>");
        }
    });

    $("#id_scale_of_score_pg").change(function() {
        var val = $(this).val();
        if (val == "0-5 CGPA") {
            $("#id_score_pg").html("<option value=''>Select</option><option value='0-1'>0-1</option><option value='1-2'>1-2</option><option value='2-3'>2-3</option><option value='3-4'>3-4</option><option value='4-5'>4-5</option>");
        } else if (val == "0-10 CGPA") {
            $("#id_score_pg").html("<option value=''>Select</option><option value='0-1'>0-1</option><option value='1-2'>1-2</option><option value='2-3'>2-3</option><option value='3-4'>3-4</option><option value='4-5'>4-5</option><option value='5-6'>5-6</option><option value='6-7'>6-7</option><option value='7-8'>7-8</option><option value='8-9'>8-9</option><option value='9-10'>9-10</option>");

        } else if (val == "0-100%") {
            $("#id_score_pg").html("<option value=''>Select</option><option value='0-10'>0-10</option><option value='10-20'>1-20</option><option value='20-30'>20-30</option><option value='30-40'>30-40</option><option value='40-50'>40-50</option><option value='50-60'>50-60</option><option value='60-70'>60-70</option><option value='70-80'>70-80</option><option value='80-90'>80-90</option><option value='90-100'>90-100</option>");
        }
    });
});
