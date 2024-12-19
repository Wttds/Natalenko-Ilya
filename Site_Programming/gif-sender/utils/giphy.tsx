import axios from 'axios';

const GIPHY_API_KEY = 'VAB1ZVV11FkociYrkerOjJ50GNjRHFMK';
const GIPHY_API_URL = 'https://api.giphy.com/v1/gifs/search';

export const fetchGif = async (query: string): Promise<string | null> => {
    try {
        const response = await axios.get(GIPHY_API_URL, {
            params: {
                api_key: GIPHY_API_KEY,
                q: query,
                limit: 1,
            },
        });
        const gifs = response.data.data;
        return gifs.length > 0 ? gifs[0].images.fixed_height.url : null;
    } catch (error) {
        console.error('Error fetching GIF:', error);
        return null;
    }
};