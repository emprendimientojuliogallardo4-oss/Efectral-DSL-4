import os
import json

class EfectralLoader:
    def __init__(self, workspace_path):
        """
        Inicializa el Loader apuntando al directorio raíz de la capa cognitiva (ej. efectral-native-v1).
        """
        self.workspace_path = workspace_path
        self.config_path = os.path.join(workspace_path, "openclaw.json")
        self.config = self._load_config()

    def _load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"No se encontró el manifiesto de OpenClaw en {self.config_path}")
        with open(self.config_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _read_efd(self, filename):
        filepath = os.path.join(self.workspace_path, filename)
        if not os.path.exists(filepath):
            return f"# [ALERTA: Archivo {filename} no encontrado]"
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read().strip()

    def build_system_prompt(self):
        """
        Ensambla y devuelve el System Prompt completo uniendo los bloques .efd 
        definidos en el workspace de openclaw.json.
        """
        workspace = self.config.get("workspace", {})
        
        # Orden de inyección estricto de Efectral Native v1
        components = [
            workspace.get("identity", "IDENTITY.efd"),
            workspace.get("soul", "SOUL.efd"),
            workspace.get("agents", "AGENTS.efd"),
            workspace.get("tools", "TOOLS.efd"),
            workspace.get("heartbeat", "HEARTBEAT.efd")
        ]

        compiled_prompt = []
        
        # 1. Cabecera de Arquitectura
        compiled_prompt.append("# ================================================================")
        compiled_prompt.append(f"# CAPA COGNITIVA: {self.config.get('name', 'Agente Efectral')}")
        compiled_prompt.append(f"# VERSION: {self.config.get('version', '1.0.0')}")
        compiled_prompt.append("# MOTOR: Efectral DSL (.efd) Nativo")
        compiled_prompt.append("# ================================================================\n")
        
        # 2. Inyección del Diccionario Sintáctico (Breve instrucción para el LLM)
        compiled_prompt.append("> DIRECTIVA ESTRICTA DEL SISTEMA (AETHIR CLAW):")
        compiled_prompt.append("> A partir de este punto, operarás bajo la arquitectura de Conjunto de Instrucciones Efectral DSL.")
        compiled_prompt.append("> Ejecuta de forma determinista las acciones (!), respeta los atributos (@), e ignora la prosa ambigua.\n")

        # 3. Ensamblaje de Bloques
        for comp in components:
            if comp:
                compiled_prompt.append(self._read_efd(comp))
                compiled_prompt.append("\n")

        return "\n".join(compiled_prompt)

    def get_runtime_hyperparameters(self):
        """
        Retorna los hiperparámetros exigidos por la capa cognitiva.
        """
        return self.config.get("runtime", {
            "temperature": 0.2,
            "topP": 0.1
        })

# Ejemplo de uso si se ejecuta directamente
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Efectral Native Loader para OpenClaw/Aethir Claw")
    parser.add_argument("--workspace", type=str, default="efectral-native-v1", help="Ruta a la carpeta de la capa cognitiva")
    args = parser.parse_args()

    loader = EfectralLoader(args.workspace)
    print("--- HYPERPARAMETERS ---")
    print(loader.get_runtime_hyperparameters())
    print("\n--- COMPILED SYSTEM PROMPT ---")
    print(loader.build_system_prompt())
