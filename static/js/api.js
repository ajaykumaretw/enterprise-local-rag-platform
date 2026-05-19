define(function () {

    async function getWelcomeMessage() {

        const response =
            await fetch("/api/dashboard");

        const data =
            await response.json();

        return data;
    }

    return {
        getWelcomeMessage:getWelcomeMessage
    };

});