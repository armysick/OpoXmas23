const puppeteer = require('puppeteer');

function delay(time) {
   return new Promise(function(resolve) { 
       setTimeout(resolve, time)
   });
}

async function refreshPage(){
    const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
    const page = await browser.newPage();
    await delay(5000);
    var url="https://<DOMAIN>/kudos/002a9ee8d4fd/";
    await page.goto(url);

    const reloadPage = async () => {
      try{
        await page.reload({ waitUntil: 'domcontentloaded' }); // Adjust options as needed
      } catch { };
    };
    const refreshInterval= 30000;

    // Set up the interval to reload the page
    const intervalId = setInterval(reloadPage, refreshInterval);
}

refreshPage();
