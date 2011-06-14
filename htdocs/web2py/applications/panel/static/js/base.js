$(document).ready(function()
{
	$('table.normal').dataTable();
  
	$('.altlayout #navigation li a').click(function(e){		
		var target = $(this).attr("href");
		if(target == '#')
		{
				$(this).parent().siblings().find("ul").slideUp("normal"); 
				$(this).next().slideToggle("normal"); // Slide down the clicked sub menu
			//$('.altlayout #navigation li a').next().slideUp();
			//$(this).next().slideToggle('normal');
		}
	});
});