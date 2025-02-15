import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000"; // Change if backend is running on a different port

export const getThreats = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/threats`);
        return response.data;
    } catch (error) {
        console.error("Error fetching threats:", error);
        return [];
    }
};

export const getMalware = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/malware`);
        return response.data;
    } catch (error) {
        console.error("Error fetching malware:", error);
        return [];
    }
};

export const getVulnerabilities = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/vulnerabilities`);
        return response.data;
    } catch (error) {
        console.error("Error fetching vulnerabilities:", error);
        return [];
    }
};

export const getAttackers = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/attackers`);
        return response.data;
    } catch (error) {
        console.error("Error fetching attackers:", error);
        return [];
    }
};
