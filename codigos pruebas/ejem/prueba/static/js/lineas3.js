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
    { year: '2020', value: 20 }
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


fetch('127.0.0.1:5000/data'){};

function timer() {

fetch('127.0.0.1:5000/data'){};
/*.then((respuesta) => {
	console.log(respuesta);
  return respuesta.json();
}).then((respuesta) => {
	console.log(respuesta);
  var nuevadataBit = [
    { year: respuesta['Bitcoinx'][0], value: respuesta['Bitcoinx'][0] },
    { year: respuesta['Bitcoinx'][1], value: respuesta['Bitcoinx'][1] },
    { year: respuesta['Bitcoinx'][2], value: respuesta['Bitcoinx'][2] },
    { year: respuesta['Bitcoinx'][3], value: respuesta['Bitcoinx'][3] },
    { year: respuesta['Bitcoinx'][4], value: respuesta['Bitcoinx'][4] }
  ]
  var nuevadataEth = [
    { year: respuesta['EthereumX'][0], value: respuesta['EthereumY'][0] },
    { year: respuesta['EthereumX'][1], value: respuesta['EthereumY'][1] },
    { year: respuesta['EthereumX'][2], value: respuesta['EthereumY'][2] },
    { year: respuesta['EthereumX'][3], value: respuesta['EthereumY'][3] },
    { year: respuesta['EthereumX'][4], value: respuesta['EthereumY'][4] }
  ]
  var nuevadataRipl = [
    { year: respuesta['RippleX'][0], value: respuesta['RippleY'][0] },
    { year: respuesta['RippleX'][1], value: respuesta['RippleY'][1] },
    { year: respuesta['RippleX'][2], value: respuesta['RippleY'][2] },
    { year: respuesta['RippleX'][3], value: respuesta['RippleY'][3] },
    { year: respuesta['RippleX'][4], value: respuesta['RippleY'][4] }
  ]
  var nuevadataLit = [
    { year: respuesta['LitecoinX'][0], value: respuesta['LitecoinY'][0] },
    { year: respuesta['LitecoinX'][1], value: respuesta['LitecoinY'][1] },
    { year: respuesta['LitecoinX'][2], value: respuesta['LitecoinY'][2] },
    { year: respuesta['LitecoinX'][3], value: respuesta['LitecoinY'][3] },
    { year: respuesta['LitecoinX'][4], value: respuesta['LitecoinY'][4] }
  ]
  var nuevadataBit_C = [
    { year: respuesta['Bitcoin_CashX'][0], value: respuesta['Bitcoin_CashY'][0] },
    { year: respuesta['Bitcoin_CashX'][1], value: respuesta['Bitcoin_CashY'][1] },
    { year: respuesta['Bitcoin_CashX'][2], value: respuesta['Bitcoin_CashY'][2] },
    { year: respuesta['Bitcoin_CashX'][3], value: respuesta['Bitcoin_CashY'][3] },
    { year: respuesta['Bitcoin_CashX'][4], value: respuesta['Bitcoin_CashY'][4] }
  ]
  var nuevadataEos = [
    { year: respuesta['EOSX'][0], value: respuesta['EOSY'][0] },
    { year: respuesta['EOSX'][1], value: respuesta['EOSY'][1] },
    { year: respuesta['EOSX'][2], value: respuesta['EOSY'][2] },
    { year: respuesta['EOSX'][3], value: respuesta['EOSY'][3] },
    { year: respuesta['EOSX'][4], value: respuesta['EOSY'][4] }
  ]

  graficaBitcoin.setData(nuevadataBit);
  graficaEthereum.setData(nuevadataEth);
  graficaRipple.setData(nuevadataRipl);
  graficaBitcoinCash.setData(nuevadataBit_C);
  graficaEos.setData(nuevadataEos);
  graficaLitecoin.setData(nuevadataLit);
})
}

setInterval('timer()',1000);*/}