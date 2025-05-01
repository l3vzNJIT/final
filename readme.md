# Lev's Web Systems Final

Due: Tuesday, April 6, 2025

# Workflow

## [branches]

1. `main` is production ready and composed of working commit
2. `develop` has all the completed features
3. `feature/*
   - Branched from `develop
   - Merged into `develop
4. `fix/*`  
   - Branched from `main`  
   - Merged into both `develop` and `main`  
5. `release/*`  
   - Branched from `develop`  
   - Merged into both `develop` and `main`  

---

## [work loop]

> **NOTE:** First set up new branches to automatically push to the origin branch with the same name:  
> `git config --global push.autoSetupRemote true`

### Adding Features
1. Create issue  
2. `git switch develop && git pull`  
3. `git switch -c feature/featureX`  
4. `git commit -s -m "I did this ... Closes #X"`  
5. `git push`  
6. On GitHub: open PR from `feature/featureX` → `develop` → merge  

### Fixing Bugs
1. Create issue  
2. `git switch main && git pull`  
3. `git switch -c fix/issueX`  
4. `git commit -s (m "I did this ... Closes #X"`)
5. `git push`  
6. On GitHub: open PR from `fix/issueX` → `main` → merge  
7. On GitHub: open PR from `fix/issueX` → `develop` → merge  

### Releasing to Main (when there are enough features)
1. `git switch develop && git pull`  
2. `git switch -c release/N && git push`  
3. On GitHub: open PR from `release/N` → `main` → merge  
4. On GitHub: open PR from `release/N` → `develop` → merge  

---


