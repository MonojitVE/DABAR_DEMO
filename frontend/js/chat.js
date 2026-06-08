// async function askAI(){

//     const input =
//         document.getElementById("question");

//     const question =
//         input.value;

//     if(!question) return;

//     const chat =
//         document.getElementById("chatWindow");

//     chat.innerHTML += `
//         <div class="message user">
//             You: ${question}
//         </div>
//     `;

//     input.value = "";

//     const response =
//         await fetch(`${API_URL}/ai-chat`,{
//             method:"POST",
//             headers:{
//                 "Content-Type":"application/json"
//             },
//             body:JSON.stringify({
//                 question
//             })
//         });

//     const data =
//         await response.json();

//     chat.innerHTML += `
//         <div class="message bot">
//             AI: ${data.answer}
//         </div>
//     `;

//     chat.scrollTop =
//         chat.scrollHeight;
// }