var graficaBitcoin = new Morris.Line({
  // ID of the element in which to draw the chart.
  element: 'graficaBitcoin',
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



var graficaEthereum = new Morris.Line({
  // ID of the element in which to draw the chart.
  element: 'graficaEthereum',
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

function timer() {

fetch('http://127.0.0.1:5000/data')
.then((respuestas) => {
  //var respuesta = JSON.stringify(respuestas);
  //console.log(respuestas);
 //respuestas.forEach((valor)=>{console.log(valor.BitcoinX)})
//console.log(respuestas[0])
  return  respuestas.json();
}).then((respuestas) => {
  //console.log(respuestas[0]['BitcoinX'][0]);
//console.log(this);  

  var nuevadataBit = [
    { year: respuestas[0]['BitcoinY'][0], value: respuestas[0]['BitcoinX'][0] },
    { year: respuestas[0]['BitcoinY'][1], value: respuestas[0]['BitcoinX'][1] },
    { year: respuestas[0]['BitcoinY'][2], value: respuestas[0]['BitcoinX'][2] },
    { year: respuestas[0]['BitcoinY'][3], value: respuestas[0]['BitcoinX'][3] },
    { year: respuestas[0]['BitcoinY'][4], value: respuestas[0]['BitcoinX'][4] }
  ]
  var nuevadataEth = [
    { year: respuestas[1]['EthereumY'][0], value: respuestas[1]['EthereumX'][0] },
    { year: respuestas[1]['EthereumY'][1], value: respuestas[1]['EthereumX'][1] },
    { year: respuestas[1]['EthereumY'][2], value: respuestas[1]['EthereumX'][2] },
    { year: respuestas[1]['EthereumY'][3], value: respuestas[1]['EthereumX'][3] },
    { year: respuestas[1]['EthereumY'][4], value: respuestas[1]['EthereumX'][4] }
  ]
  var nuevadataRipl = [
    { year: respuestas[2]['RippleY'][0], value: respuestas[2]['RippleX'][0] },
    { year: respuestas[2]['RippleY'][1], value: respuestas[2]['RippleX'][1] },
    { year: respuestas[2]['RippleY'][2], value: respuestas[2]['RippleX'][2] },
    { year: respuestas[2]['RippleY'][3], value: respuestas[2]['RippleX'][3] },
    { year: respuestas[2]['RippleY'][4], value: respuestas[2]['RippleX'][4] }
  ]
  var nuevadataLit = [
    { year: respuestas[3]['LitecoinY'][0], value: respuestas[3]['LitecoinX'][0] },
    { year: respuestas[3]['LitecoinY'][1], value: respuestas[3]['LitecoinX'][1] },
    { year: respuestas[3]['LitecoinY'][2], value: respuestas[3]['LitecoinX'][2] },
    { year: respuestas[3]['LitecoinY'][3], value: respuestas[3]['LitecoinX'][3] },
    { year: respuestas[3]['LitecoinY'][4], value: respuestas[3]['LitecoinX'][4] }
  ]
  var nuevadataBit_C = [
    { year: respuestas[4]['Bitcoin_CashY'][0], value: respuestas[4]['Bitcoin_CashX'][0] },
    { year: respuestas[4]['Bitcoin_CashY'][1], value: respuestas[4]['Bitcoin_CashX'][1] },
    { year: respuestas[4]['Bitcoin_CashY'][2], value: respuestas[4]['Bitcoin_CashX'][2] },
    { year: respuestas[4]['Bitcoin_CashY'][3], value: respuestas[4]['Bitcoin_CashX'][3] },
    { year: respuestas[4]['Bitcoin_CashY'][4], value: respuestas[4]['Bitcoin_CashX'][4] }
  ]
  var nuevadataEos = [
    { year: respuestas[5]['EOSY'][0], value: respuestas[5]['EOSX'][0] },
    { year: respuestas[5]['EOSY'][1], value: respuestas[5]['EOSX'][1] },
    { year: respuestas[5]['EOSY'][2], value: respuestas[5]['EOSX'][2] },
    { year: respuestas[5]['EOSY'][3], value: respuestas[5]['EOSX'][3] },
    { year: respuestas[5]['EOSY'][4], value: respuestas[5]['EOSX'][4] }
  ]
    console.log(nuevadataEos);
//console.log(nuevadataBit_C );
//console.log(nuevadataLit);
//console.log(nuevadataRipl);
//console.log(nuevadataEth);
//console.log(nuevadataBit);
  graficaBitcoin.setData(nuevadataBit);
  graficaEthereum.setData(nuevadataEth);
  graficaRipple.setData(nuevadataRipl);
  graficaBitcoinCash.setData(nuevadataBit_C);
  graficaEos.setData(nuevadataEos);
  graficaLitecoin.setData(nuevadataLit);
})
}

setInterval('timer()',1800000);