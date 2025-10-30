export const API_BASE_URL = "http://localhost:8000";

export async function fetchEmployees() {
  const response = await fetch(`${API_BASE_URL}/reports/employees`);
  if (!response.ok) {
    throw new Error("Erro ao buscar relatório de funcionários");
  }
  return response.json();
}
