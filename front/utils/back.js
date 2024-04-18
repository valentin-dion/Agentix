/**
 * Sends a GET or POST request to a specified endpoint.
 * @param {string} endpoint - The endpoint to fetch.
 * @param {Object} [body] - Optional body for POST request.
 * @returns {Promise<Object|Array>} - A promise resolving to the parsed JSON response.
 */
async function back(endpoint, body) {
    const url = `http://localhost:5000/${endpoint}`;
    const options = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    if (body) {
        options.method = 'POST';
        options.body = JSON.stringify(body);
    } else {
        options.method = 'GET';
    }

    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Failed to fetch:', error);
        throw error;
    }
}

export {back};