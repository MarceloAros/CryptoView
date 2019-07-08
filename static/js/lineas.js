var graficaBitcoin = new Morris.Line({
  // ID of the element in which to draw the chart.
  element: 'graficaBitcoin',
  // Chart data records -- each entry in this array corresponds to a point on
  // the chart.
  data: [
    { Hora: '08', value: 20 },
    { Hora: '09', value: 10 },
    { Hora: '10', value: 5 },
    { Hora: '11', value: 5 },
    { Hora: '12', value: 20 }
  ],
  // The name of the data record attribute that contains x-values.
  xkey: 'year',
  // A list of names of data record attributes that contain y-values.
  ykeys: ['value'],
  // Labels for the ykeys -- will be displayed when you hover over the
  // chart.
  labels: ['Value'],
  resize: true
});

var id = ['graficaBitcoin','graficaEthereum', 'graficaRipple', 'graficaBitcoinCash', 'graficaEos','graficaLitecoin']

//var d = x;

//d.el = id[1];
//console.log(id[1]);
//for (var i = 0; i < id.length; i++) {
  //x[i] = new Morris.Line()
  //x[i].element=id[i];
  //console.log("hola");
//}
//Morris.setData(data nueva);
var graficaEthereum = new Morris.Line({
  // ID of the element in which to draw the chart.
  element: 'graficaEthereum',
  // Chart data records -- each entry in this array corresponds to a point on
  // the chart.
  data: [
    { Hora: '08', value: 20 },
    { Hora: '09', value: 10 },
    { Hora: '10', value: 5 },
    { Hora: '11', value: 5 },
    { Hora: '12', value: 20 }
  ],
  // The name of the data record attribute that contains x-values.
  xkey: 'year',
  // A list of names of data record attributes that contain y-values.
  ykeys: ['value'],
  // Labels for the ykeys -- will be displayed when you hover over the
  // chart.
  labels: ['Value'],
  resize: true
});
var graficaRipple = new Morris.Line({
  // ID of the element in which to draw the chart.
  element: 'graficaRipple',
  // Chart data records -- each entry in this array corresponds to a point on
  // the chart.
  data: [
    { year: '2008', value: 20 },
    { year: '2009', value: 10 },
    { year: '2010', value: 5 },
    { year: '2011', value: 5 },
    { year: '2012', value: 20 }
  ],
  // The name of the data record attribute that contains x-values.
  xkey: 'year',
  // A list of names of data record attributes that contain y-values.
  ykeys: ['value'],
  // Labels for the ykeys -- will be displayed when you hover over the
  // chart.
  labels: ['Value'],
  resize: true
});
var graficaBitcoinCash = new Morris.Line({
  // ID of the element in which to draw the chart.
  element: 'graficaBitcoinCash',
  // Chart data records -- each entry in this array corresponds to a point on
  // the chart.
  data: [
    { year: '2008', value: 20 },
    { year: '2009', value: 10 },
    { year: '2010', value: 5 },
    { year: '2011', value: 5 },
    { year: '2012', value: 20 }
  ],
  // The name of the data record attribute that contains x-values.
  xkey: 'year',
  // A list of names of data record attributes that contain y-values.
  ykeys: ['value'],
  // Labels for the ykeys -- will be displayed when you hover over the
  // chart.
  labels: ['Value'],
  resize: true
});
var graficaEos = new Morris.Line({
  // ID of the element in which to draw the chart.
  element: 'graficaEos',
  // Chart data records -- each entry in this array corresponds to a point on
  // the chart.
  data: [
    { year: '2008', value: 20 },
    { year: '2009', value: 10 },
    { year: '2010', value: 5 },
    { year: '2011', value: 5 },
    { year: '2012', value: 20 }
  ],
  // The name of the data record attribute that contains x-values.
  xkey: 'year',
  // A list of names of data record attributes that contain y-values.
  ykeys: ['value'],
  // Labels for the ykeys -- will be displayed when you hover over the
  // chart.
  labels: ['Value'],
  resize: true
});
var graficaLitecoin = new Morris.Line({
  // ID of the element in which to draw the chart.
  element: 'graficaLitecoin',
  // Chart data records -- each entry in this array corresponds to a point on
  // the chart.
  data: [
    { year: '2008', value: 20 },
    { year: '2009', value: 10 },
    { year: '2010', value: 5 },
    { year: '2011', value: 5 },
    { year: '2012', value: 20 }
  ],
  // The name of the data record attribute that contains x-values.
  xkey: 'year',
  // A list of names of data record attributes that contain y-values.
  ykeys: ['value'],
  // Labels for the ykeys -- will be displayed when you hover over the
  // chart.
  labels: ['Value'],
  resize: true
});