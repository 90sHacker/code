let smsData = {};
cacheData = {
  amount: {
    k1: 10,
    k2: 35
  },
  validity: {
    k1: 3,
    k2: 4
  },
  msisdn: {
    k1: '08939304',
    k2: '089304',
  }
}
for(const key in cacheData) {
  smsData = cacheData[key] 
  console.log(smsData);
}
