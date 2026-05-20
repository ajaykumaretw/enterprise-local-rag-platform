define(['math', 'message', 'api'],function(math,message,api) {
        
        async function initialize() {
            console.log(

                "RequireJS Loaded Successfully"
            );
            // =================================
            // Test RequireJS Button
            // =================================
        
            const btn = document.getElementById("btn");
            btn.addEventListener("click",function() {
                    alert("Flask + RequireJS Working");
                }
            );

            // =================================
            // Dashboard API
            // =================================
            const flaskMessage = await api.getWelcomeMessage();
            console.log(flaskMessage);
            console.log(math.add(10, 20)
            );

            console.log(message.welcome(flaskMessage.developer));

            // =================================
            // Upload PDF Event
            // =================================
        document.getElementById("uploadBtn").addEventListener("click", async function() {
            const file =document.getElementById("pdfFile").files[0];
                   if (!file) {
                       alert("Please select PDF file");return;
                   }
                    const formData =new FormData();
                    formData.append("file",file);
                    try {
                        const response =
                            await fetch( "/api/upload", {
                                    method: "POST",
                                    body: formData
                                }
                            );
                        const result =await response.json();
                        console.log(result);
                        alert( result.message);
                    } catch (error) {
                        console.error(error);
                        alert("PDF upload failed");
                    }
                }
            );
            // =================================
            // Ask AI Event
            // =================================

            document.getElementById("askBtn").addEventListener("click",async function() {
                    const question =document.getElementById("question").value;
                    if (!question) {
                        alert("Please enter question");
                        return;
                    }
                    try {

                        document.getElementById("answer").innerHTML ="Thinking...";
                        const response =await fetch("/api/ask",{
                            method: "POST",headers: {
                                    "Content-Type": "application/json"
                                    },
                                    body: JSON.stringify({
                                        question: question
                                    })
                                }
                            );
                        const result =await response.json();
                        console.log(result);
                        document.getElementById("answer").innerHTML =result.answer;
                    } catch (error) {
                        console.error(error);
                        document.getElementById("answer").innerHTML = "AI request failed";
                    }
                }
            );
        }
        return {
            initialize: initialize
        };
    }
);