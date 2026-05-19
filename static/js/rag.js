define(function () {

    async function uploadPDF(file) {

        const formData = new FormData();

        formData.append("file", file);

        const response =
            await fetch("/api/upload", {

                method: "POST",

                body: formData

            });

        return await response.json();
    }


    async function askQuestion(question) {

        const response =
            await fetch("/api/ask", {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    question: question
                })

            });

        return await response.json();
    }

    return {

        uploadPDF: uploadPDF,

        askQuestion: askQuestion
    };

});