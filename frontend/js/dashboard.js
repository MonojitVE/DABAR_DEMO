// window.onload = async () => {

//     loadDashboard();
//     loadTransactions();

// };

// async function loadDashboard(){

//     const response =
//         await fetch(`${API_URL}/dashboard`);

//     const data =
//         await response.json();

//     document.getElementById("income").innerText =
//         `₹${data.total_income}`;

//     document.getElementById("expense").innerText =
//         `₹${data.total_expenses}`;

//     document.getElementById("balance").innerText =
//         `₹${data.balance}`;

//     createChart(data.category_breakdown);
// }

// async function loadTransactions(){

//     const response =
//         await fetch(`${API_URL}/transactions`);

//     const transactions =
//         await response.json();

//     const table =
//         document.getElementById("transactionTable");

//     table.innerHTML = "";

//     transactions.forEach(tx => {

//         table.innerHTML += `
//         <tr>
//             <td>${tx.date}</td>
//             <td>${tx.description}</td>
//             <td>${tx.category}</td>
//             <td>${tx.source}</td>
//             <td>₹${tx.amount}</td>
//         </tr>
//         `;

//     });
// }

// function createChart(data){

//     new Chart(
//         document.getElementById("expenseChart"),
//         {
//             type:"doughnut",
//             data:{
//                 labels:Object.keys(data),
//                 datasets:[{
//                     data:Object.values(data)
//                 }]
//             }
//         }
//     );
// }