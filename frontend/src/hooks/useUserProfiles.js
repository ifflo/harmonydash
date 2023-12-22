// src/hooks/useUserProfiles.js
import { useState, useEffect } from 'react';
import { getUserProfiles } from '../services/apiService';

const useUserProfiles = () => {
    const [userProfiles, setUserProfiles] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        let isMounted = true;

        getUserProfiles()
            .then(response => {
                if (isMounted) {
                    setUserProfiles(response.data);
                    setLoading(false);
                }
            })
            .catch(error => {
                if (isMounted) {
                    console.error('Error fetching user profiles!', error);
                    setError(error);
                    setLoading(false);
                }
            });

        return () => {
            isMounted = false;
        };
    }, []);

    return { userProfiles, loading, error };
};

export default useUserProfiles;
