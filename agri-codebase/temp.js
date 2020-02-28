obj = {
  "Almond Tree": "1.0060214e-17",
  Banana: "5.5214714e-31",
  Beans: "1.7517032e-23",
  "Bell Peppers": "7.4391235e-28",
  Broccoli: "1.8180927e-26",
  Canola: "8.4827315e-27",
  Carrot: "1.2416092e-14",
  Corn: "7.3218424e-11",
  Cotton: "3.9136056e-13",
  Flax: "7.653623e-15",
  Onion: "1.254715e-10",
  Peanuts: "6.9086686e-16",
  "Pecan Tree": "2.7030705e-38",
  Potato: "5.8100054e-32",
  Rice: "5.3785855e-32",
  Soybean: "3.198974e-23",
  Sugarbeets: "1.0",
  Sugarcane: "9.128412e-22",
  Sunflower: "2.3221658e-27",
  "Walnut Tree": "0.0",
  Wheat: "8.65351e-18"
};

var arr = Object.entries(obj);
// arr.forEach((data) => {
// //   x = data[0];
// //   y = data[1];

// //   console.log(x[0]);
// });

function sortFunction(a, b) {
  if (a[1] === b[1]) {
    return 0;
  } else {
    return a[1]  b[1] ? -1 : 1;
  }
}

console.log(arr.sort(sortFunction));
