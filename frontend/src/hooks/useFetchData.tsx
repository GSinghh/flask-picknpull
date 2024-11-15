import { useState, useEffect } from "react";

export function useFetchData<T>(url: string): {
    data: T | null;
    loading: boolean;
    error: string | null;
} {
    const [data, setData] = useState<T | null>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(url);
                if (!response) {
                    throw new Error("Error while fetching data");
                }
                const data = await response.json();
                setData(data);
            } catch (error: any) {
                setError(error.message || "An Error Occurred");
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [url]);
    return { data, loading, error };
}
