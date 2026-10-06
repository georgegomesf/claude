const { chromium } = require('/opt/node-tools/node_modules/playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1200, height: 1500 } });
  await p.goto('file://' + path.resolve(__dirname, 'cards.html'));
  await p.evaluate(() => document.fonts.ready);
  for (let i = 1; i <= 10; i++) {
    const id = 'c' + String(i).padStart(2, '0');
    await p.locator('#' + id).screenshot({ path: path.resolve(__dirname, 'png', `card-${String(i).padStart(2, '0')}.png`) });
  }
  await b.close();
})();
