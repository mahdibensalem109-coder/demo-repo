import asyncio
import time

async def tache_longue():
    print("--- Tâche Longue : Je commence (4s d'attente) ---")
    # Ici, je relâche le contrôle de l'Event Loop
    await asyncio.sleep(4) 
    print("--- Tâche Longue : J'ai enfin fini ! ---")

async def tache_courte():
    print("Tâche Courte : Je commence (2s d'attente)")
    await asyncio.sleep(2)
    print("Tâche Courte : Je suis déjà finie !")

async def main():
    start = time.time()
    
    print("Début du service...")
    # On lance les deux en même temps
    await asyncio.gather(tache_longue(), tache_courte())
    
    end = time.time()
    print(f"\nTemps total : {end - start:.2f} secondes")

asyncio.run(main())