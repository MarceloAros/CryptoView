 google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        fetch('127.0.0.1:5000/data')
        .then((respuesta) => {
        return respuesta.json();
        }).then((respuesta) => {
        var data = google.visualization.arrayToDataTable([
          [respuesta['BitcoinX'][0], respuesta['BitcoinY'][0]],
          [respuesta['BitcoinX'][1], respuesta['BitcoinY'][1]],
          [respuesta['BitcoinX'][2], respuesta['BitcoinY'][2]],
          [respuesta['BitcoinX'][3], respuesta['BitcoinY'][3]],
          [respuesta['BitcoinX'][4], respuesta['BitcoinY'][4]]
        ]);

        var options = {
          title: 'Company Performance',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('graficaBitcoin'));

        chart.draw(data, options);
      
    })}
