function my_chart()
{
if (chartType == 'Bar'){
	var mydata;
	nv.addGraph(function() {
      for (var i=1; i<6; i++){
      d3.select('#chart' + String(i) + ' svg')
       .remove();
      d3.scale.linear(0.01);
       if(i==1){
       		$('#chart' + String(i)).html("<svg style=\"height: 300px;\"></svg>");	
       }
       else
       {
       	$('#chart' + String(i)).html("<svg style=\"height: 180px;\"></svg>");
       }

      chart = nv.models.discreteBarChart()
          .x(function(d) { return d.label })
          .y(function(d) { return d.value })
          .staggerLabels(true)
          .showValues(true)
      chart.xAxis
      		.axisLabel('year')
      	   .tickFormat(d3.format('2d'));

  	  /*chart.yAxis.axisLabel('');      */
            if (i ==1) {
              mydata = charta;
            }
            if (i ==2) {
              mydata = chartb;
            }
            if (i ==3) {
              mydata = chartc;
            }
            if (i ==4) {
              mydata = chartd;
            }
            if (i ==5) {
              mydata = charte;
            }
      d3.select('#chart' + String(i) + ' svg')
          .datum(mydata)
        .transition().duration(500)
          .call(chart);
       nv.utils.windowResize(chart.update);
    }
      return chart;
    });
}
else
{
	var mydata;
nv.addGraph(function() {
  for (var i=1; i<6; i++ ){
	      d3.select('#chart' + String(i) + ' svg')
   .remove();
   if(i==1){
   		$('#chart' + String(i)).html("<svg style=\"height: 300px;\"></svg>");	
   }
   else
   {
   	$('#chart' + String(i)).html("<svg style=\"height: 180px;\"></svg>");
   }
  chart = nv.models.lineChart();
  chart.xAxis
      .axisLabel('year')
      .tickFormat(d3.format('2d'));

  chart.yAxis
      .axisLabel('EDI')
      .tickFormat(d3.format('.02f'));
      if (i ==1) {
        mydata = charta;
      }
      if (i ==2) {
        mydata = chartb;
      }
      if (i ==3) {
        mydata = chartc;
      }
      if (i ==4) {
        mydata = chartd;
      }
      if (i ==5) {
        mydata = charte;
      }
      d3.select('#chart' + String(i) + ' svg')
        .datum(mydata)
        .transition().duration(500)
        .call(chart);
       nv.utils.windowResize(chart.update);
    }
    return chart;
  });

}
}


function chart_ratio_of_pr_upr (data) {
if (chartType=='Line'){
	d3.select('#chartROfPToUp  svg')
       .remove();
    $('#chartROfPToUp').html("<svg style=\"height: 300px;\"></svg>");
		var newData = [];
		var years = [2007,2008,2009,2010,2011];
		for(var a in years){
				newData.push({x:String(years[a]),y:data.values[String(years[a])]})
		}
		nv.addGraph(function() {
		var chart = nv.models.lineChart();
		chart.xAxis
		  .axisLabel('year')
		  .tickFormat(d3.format('2d'));
		chart.yAxis
		  .axisLabel('Ratio')
		  .tickFormat(d3.format('.02f'));
		d3.select('#chartROfPToUp svg')
		  .datum(
		  		[{
		  			values:newData,
		  			'area':true,
		  			key:'Ratio of Primary to Upper Primary School in ' + selectedDistrict,
		  			color:'#ff7f0e'
		  		}]
		  	)
		.transition().duration(1000)
		 .call(chart);
		nv.utils.windowResize(chart.update);
		return chart;
		});
}
else{
	d3.select('#chartROfPToUp  svg')
       .remove();
    $('#chartROfPToUp').html("<svg style=\"height: 300px;\"></svg>");
		var newData = [];
		var years = [2007,2008,2009,2010,2011];
		for(var a in years){
				newData.push({'label':years[a],'value':data.values[String(years[a])]})
		}
		nv.addGraph(function() {
      chart = nv.models.discreteBarChart()
          .x(function(d) { return d.label })
          .y(function(d) { return d.value })
          .staggerLabels(true)
          .showValues(true)
      chart.xAxis.axisLabel('year');
      chart.yAxis.axisLabel('Ratio');
		d3.select('#chartROfPToUp svg')
		  .datum(
		  		[{
		  			values:newData,
		  			key:'Ratio of Primary to Upper Primary School in ' + selectedDistrict,
		  			color:'#ff7f0e'
		  		}]
		  	)
		.transition().duration(1000)
		 .call(chart);
		nv.utils.windowResize(chart.update);
		return chart;
		});
}
}

function chart_avg_school_student_ratio (data) {
	if (chartType=='Line'){
	d3.select('#chartASSR  svg')
       .remove();
    $('#chartASSR').html("<svg style=\"height: 300px;\"></svg>");
		var newData = [];
		var years = [2007,2008,2009,2010,2011];
		for(var a in years){
				newData.push({x:String(years[a]),y:1/(data.values[String(years[a])])})
		}
		nv.addGraph(function() {
		var chart = nv.models.lineChart();
		chart.xAxis
		  .axisLabel('year')
		  .tickFormat(d3.format('2d'));
		chart.yAxis
		  .axisLabel('Ratio')
		  .tickFormat(d3.format('.02f'));
		d3.select('#chartASSR svg')
		  .datum(
		  		[{
		  			values:newData,
		  			'area':true,
		  			key:'School Student Ratio in ' + selectedDistrict,
		  			color:'#ff7f0e'
		  		}]
		  	)
		.transition().duration(1000)
		 .call(chart);
		nv.utils.windowResize(chart.update);
		return chart;
		});
}
else{
		d3.select('#chartASSR  svg')
       		.remove();
    	$('#chartASSR').html("<svg style=\"height: 300px;\"></svg>");
		var newData = [];
		var years = [2007,2008,2009,2010,2011];
		for(var a in years){
				newData.push({'label':years[a],'value':1/(data.values[String(years[a])])})
		}
		nv.addGraph(function() {
      chart = nv.models.discreteBarChart()
          .x(function(d) { return d.label })
          .y(function(d) { return d.value })
          .staggerLabels(true)
          .showValues(true)
      chart.xAxis.axisLabel('year');
      chart.yAxis.axisLabel('Ratio');
		d3.select('#chartASSR svg')
		  .datum(
		  		[{
		  			values:newData,
		  			key:'School Student Ratio in ' + selectedDistrict,
		  		}]
		  	)
		.transition().duration(1000)
		 .call(chart);
		nv.utils.windowResize(chart.update);
		return chart;
		});
}
}
function chart_outcome (data,key) {
	if (chartType=='Line'){
	d3.select('#chartOutcome  svg')
       .remove();
    $('#chartOutcome').html("<svg style=\"height: 300px;\"></svg>");
		var newData = [];
		var years = [2007,2008,2009,2010,2011];
		for(var a in years){
				newData.push({x:String(years[a]),y:(data.values[String(years[a])])})
		}
		nv.addGraph(function() {
		var chart = nv.models.lineChart();
		chart.xAxis
		  .axisLabel('year')
		  .tickFormat(d3.format('2d'));
		chart.yAxis
		  .axisLabel('Ratio')
		  .tickFormat(d3.format('.02f'));
		d3.select('#chartOutcome svg')
		  .datum(
		  		[{
		  			values:newData,
		  			'area':true,
		  			key:key,
		  			color:'#ff7f0e'
		  		}]
		  	)
		.transition().duration(1000)
		 .call(chart);
		nv.utils.windowResize(chart.update);
		return chart;
		});
}
else{
		d3.select('#chartOutcome  svg')
       		.remove();
    	$('#chartOutcome').html("<svg style=\"height: 300px;\"></svg>");
		var newData = [];
		var years = [2007,2008,2009,2010,2011];
		for(var a in years){
				newData.push({'label':years[a],'value':(data.values[String(years[a])])})
		}
		nv.addGraph(function() {
      chart = nv.models.discreteBarChart()
          .x(function(d) { return d.label })
          .y(function(d) { return d.value })
          .staggerLabels(true)
          .showValues(true)
      chart.xAxis.axisLabel('year');
      chart.yAxis.axisLabel('Ratio');
		d3.select('#chartOutcome svg')
		  .datum(
		  		[{
		  			values:newData,
		  			key:key,
		  		}]
		  	)
		.transition().duration(1000)
		 .call(chart);
		nv.utils.windowResize(chart.update);
		return chart;
		});
}
}
function chart_teacher (data,key) {
	if (chartType=='Line'){
	d3.select('#chartTeacher  svg')
       .remove();
    $('#chartTeacher').html("<svg style=\"height: 300px;\"></svg>");
		var newData = [];
		var years = [2007,2008,2009,2010,2011];
		for(var a in years){
				newData.push({x:String(years[a]),y:(data.values[String(years[a])])})
		}
		nv.addGraph(function() {
		var chart = nv.models.lineChart();
		chart.xAxis
		  .axisLabel('year')
		  .tickFormat(d3.format('2d'));
		chart.yAxis
		  .axisLabel('Ratio')
		  .tickFormat(d3.format('.02f'));
		d3.select('#chartTeacher svg')
		  .datum(
		  		[{
		  			values:newData,
		  			'area':true,
		  			key:key,
		  			color:'#ff7f0e'
		  		}]
		  	)
		.transition().duration(1000)
		 .call(chart);
		nv.utils.windowResize(chart.update);
		return chart;
		});
}
else{
		d3.select('#chartTeacher  svg')
       		.remove();
    	$('#chartTeacher').html("<svg style=\"height: 300px;\"></svg>");
		var newData = [];
		var years = [2007,2008,2009,2010,2011];
		for(var a in years){
				newData.push({'label':years[a],'value':(data.values[String(years[a])])})
		}
		nv.addGraph(function() {
      chart = nv.models.discreteBarChart()
          .x(function(d) { return d.label })
          .y(function(d) { return d.value })
          .staggerLabels(true)
          .showValues(true)
      chart.xAxis.axisLabel('year');
      chart.yAxis.axisLabel('Ratio');
		d3.select('#chartTeacher svg')
		  .datum(
		  		[{
		  			values:newData,
		  			key:key,
		  		}]
		  	)
		.transition().duration(1000)
		 .call(chart);
		nv.utils.windowResize(chart.update);
		return chart;
		});
}
}