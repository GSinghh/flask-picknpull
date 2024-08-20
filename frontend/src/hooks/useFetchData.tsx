import { useState, useEffect } from "react";

type CPUData = {
    cpuUsage: number;
    cpuFreq: number[];
    loadAvg: number[];
    responseCode: number;
};
type MemData = {
    [key: string]: string | number;
    responseCode: number;
};
type Error = {
    message: string | number | null;
    responseCode: number;
};
type fetchDataState = {
    data: CPUData | MemData | Error | null;
    loading: boolean;
    error: string | null;
};
export function useFetchData(url: string): fetchDataState {
    const [data, setData] = useState<CPUData | MemData | Error | null>(null);
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
                setError(error);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [url]);
    return { data, loading, error };
}
