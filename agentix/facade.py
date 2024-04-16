class Agentix:
    """Facade to a lot of moving parts
    """
    
    @staticmethod
    def all_endpoints_full() -> str:
        """Meant to be use by gen1 agents.
        return all the endpoints with internal state
        """