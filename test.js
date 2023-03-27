const { DateTime } = require("luxon");
// function generateId() {
// 	return DateTime.local().startOf('day').plus({ hours: 1 }).ts;
// }

function generateId() {
	console.log(new Date().valueOf());
}

function generateNewId() {
	console.log(DateTime.now().plus({ days: -2, minutes: 960 }).ts);
	// console.log(DateTime.fromISO("20160525"));
	// const validity = DateTime.fromISO("20230525");
	// const time = DateTime.local()
	// console.log("TIME", time);
	// //console.log(DateTime.fromISO(time));

	// let diff = validity.diff(time, "months")
	// console.log("DIFF", diff.toObject())
	// diff = diff.toObject();

	// if (Math.round(diff.months) >= 6) console.log("Greater than 6 months!")

	console.log(DateTime.local().startOf('day').plus({ hours: -1 }).ts);
	console.log(DateTime.local().startOf('day').plus({ hours: 1 }).ts);
	console.log(DateTime.local().endOf('day').plus({ hours: 1 }).ts);
}


const transactionId = 22

// const delay = (duration) => {
//   return new Promise((resolve) => setTimeout(resolve, duration));
// };

// const generateTransactionId = setTimeout(() => {
// 	const date = new Date()
// 	const day = (`0${date.getMonth() + 1}`).slice(-2)
// 	const hour = date.getHours()
// 	const minute = (`0${date.getMinutes() + 1}`).slice(-2)
// 	console.log(minute)
// 	const seconds = (`0${date.getSeconds() + 1}`).slice(-2)
// 	const id = transactionId + 1
// 	const getTransactionSerial = number => (number <= 9999999 ? `000000${number}`.slice(-7) : number)

// 	return `aggregatorId${date.getFullYear()}${date.getMonth()}${day}${hour}${minute}${seconds}${getTransactionSerial(id)}`
// }, 1000)


// body = {
// 	txId: generateTransactionId
// }
// console.log(body);

generateNewId()
//generateId();

