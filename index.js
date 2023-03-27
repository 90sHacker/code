
const _axios = require("axios").create({
  baseURL: 'https://staging-gateway.iykejordanlimited.com/products/',
  headers: {
      "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoIjp7ImVtYWlsVmVyaWZpZWRBdCI6bnVsbCwicGhvbmVWZXJpZmllZEF0IjpudWxsLCJ1c2VySWQiOiI1ZGY3ODQzMThhNDdlNDAwMWJlZTU4MjciLCJyb2xlIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluQHRlbGVjb21tZS5jb20iLCJub3RpZmljYXRpb25MYXN0UmVhZEF0IjoiMjAyMC0wMy0xMlQxMjoyMzo0NC4yMTRaIiwiYXV0aElkIjoiNWRmNzg0MzI4YTQ3ZTQwMDFiZWU1ODJhIiwicHJvZmlsZSI6eyJuYW1lIjoiVGVsZWNvbW1lIEFkbWluIiwiZW1haWwiOiJhZG1pbkB0ZWxlY29tbWUuY29tIiwicGhvbmVOdW1iZXIiOiIrMjM0NzAxMjM0NTY3OCIsInVzZXJJZCI6IjVkZjc4NDMxOGE0N2U0MDAxYmVlNTgyNyJ9LCJub3RpZmljYXRpb25zIjpbeyJkZXNjcmlwdGlvbiI6IkFjY291bnQgQXBwcm92YWxzOiAyIHByb3ZpZGVyKHMpIGFyZSBhd2FpdGluZyBhcHByb3ZhbCIsImxldmVsIjoid2FybmluZyJ9XSwidW5yZWFkIjp7InRpY2tldHMiOjAsInByb2R1Y3RzIjoxNTR9fSwiaWF0IjoxNTg1Mzg0Nzg2LCJhdWQiOiJ2YXMtYWdnIiwiaXNzIjoidmFzLWF1dGgiLCJzdWIiOiJ2YXMtYWdnIn0.T5H42csX4L4rVM9Om9fr_fNulZU8vSCeC-jif-tm-XS96Z5Ncq0Npv_fHnw78S5Uq6uJW9gK-AMfvPFfkWBsZg",
  },
});

const helper = async () => {
  let sender = '64620';
  let messageContent = "There are no products configured for " + sender;
  let network = '9mobile'
  const data = await _axios.get('api/v1/configurations/channels?shortCode=64620&channel=sms&network=9mobile').catch(e => console.log(e.message));

  console.log('configured data', data.data.data)
  console.log('DATATA', data.data.data.length)
  if (data.data.data.length > 0) {
      messageContent = '';
      for (let config of data.data.data) {
          let content = "";
          let middleContent = '';
          let cost = '';
          let holder = '';
          const plans = config.plans || [];
          // console.log("Config", config, plans);
          for (let plan of plans) {

              // const productDetails = (await productService.getProductDetails({ productId: plan.productId })).data

              // console.log("product details dey here", productDetails)

              // hack TODO: remove check for undefined later
              if (typeof plan?.networkConfig !== 'undefined') {
                  // if (isEmpty(plan?.networkConfig[network]))
                  //     continue;

                  //-------------------------------------------------------------
                  const { smsKeyword, ussdAccessString } = plan.networkConfig[network];

                  const day = (plan.validity === 1) ? 'day' : 'days';
                  // SMS
                  if (smsKeyword && smsKeyword !== '' && smsKeyword !== 'n/a' && !ussdAccessString || ussdAccessString == '') {
                      holder = `text ${smsKeyword} to ${sender},`;
                  }

                  // USSD
                  console.log('this is network', network)
                  let flag = true;
                  if (ussdAccessString && ussdAccessString !== '' && !smsKeyword || smsKeyword == '' || smsKeyword === 'n/a') {
                      flag = false;
                      holder = `dial *${sender}#,`;
                      console.log('this is holder...', holder);
                  }
                  
                  // Both SMS
                  if (smsKeyword && (smsKeyword !== '' && smsKeyword !== 'n/a') && ussdAccessString && ussdAccessString !== '') {
                      holder = `text ${smsKeyword} to ${sender}`;
                  }
                  console.log('this is holder again...', holder);
                  
                  if (network == '9mobile' && flag) {
                      if (plans.length === 1) {
                          console.log('ONE PLAN----')
                          content = `To subscribe for ${plan.name.toUpperCase()}, ${holder}`;

                          cost = `service costs N${plan.amount}/${plan.validity} ${day}`
                      } else {
                          console.log('MULTIPLE PLANS')
                          if (content === '') {
                              console.log('FIRST LOOP FOR MULTIPLE PLANS......');
                              content = `To subscribe for ${plan.name.toUpperCase()}, ${holder}`;
                              cost = `services costs N${plan.amount}/${plan.validity} ${day}`;

                          } else {
                              console.log('SUBSEQUENT LOOP FOR MULTIPLE PLANS......');

                              middleContent += ` for ${plan.name.toUpperCase()} ${holder}`;
                              cost += `, ₦${plan.amount}/${plan.validity} ${day}`;
                          }
                      }
                  }
                  else if (network != '9mobile') {
                      if (plans.length === 1) {
                          console.log('ONE PLAN----')
                          content = `To subscribe for ${plan.name.toUpperCase()}, ${holder}`;

                          cost = `service costs N${plan.amount}/${plan.validity} ${day}`
                      } else {
                          console.log('MULTIPLE PLANS')
                          if (content === '') {
                              console.log('FIRST LOOP FOR MULTIPLE PLANS......');
                              content = `To subscribe for ${plan.name.toUpperCase()}, ${holder}`;
                              cost = `services costs N${plan.amount}/${plan.validity} ${day}`;

                          } else {
                              console.log('SUBSEQUENT LOOP FOR MULTIPLE PLANS......');

                              middleContent += ` for ${plan.name.toUpperCase()} ${holder}`;
                              cost += `, ₦${plan.amount}/${plan.validity} ${day}`;
                          }
                      }
                  }
                  // content = `${content} ${middleContent} ${holder2} ${cost}. TEXT STOP to ${sender} to unsubscribe.` 

                  //-------------------------------------------------------------


                  console.log("Config Plan", plan);
                  // content += `To subscribe for ${plan.name.toUpperCase()} plan, Text ${smsKeyword} to ${sender} service costs ₦${plan.amount}/${plan.validity} days. Text STOP to 64620 to unsubscribe.`;
                  // console.log("Content", content);

                  // if (network == "mtn" && !res.smsMTID)
                  //     res.smsMTID = plan.networkConfig[network].smsMTID;
              }

          }

          if (content !== '') {
              content += `${middleContent} ${cost}. Text ${config.sms[network].unsubscriptionKeyword} to ${sender} to unsubscribe.`;
              messageContent += content;
          };


    }
    console.log(messageContent);
  };
}

helper();