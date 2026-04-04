const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export async function fetchJson(endpoint, options = {}) {
  const isFormMethod =
    options.method && options.method !== "GET" && options.method !== "HEAD";

  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers: {
      ...(isFormMethod ? { "Content-Type": "application/json" } : {}),
      ...(options.headers || {}),
    },
  });

  if (!response.ok) {
    throw new Error(`API request failed: ${response.status}`);
  }

  return response.json();
}

export { API_BASE_URL };